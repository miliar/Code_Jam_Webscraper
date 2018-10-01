#reading file
with open("C-small-2-attempt0.in") as z:
    casenumber = int(z.readline())
    
    #case!
    for case in range(1,casenumber+1):

    
        #reading file
        data = z.readline().strip().split(" ")

        N = int(data[0])
        K = int(data[1])
        #def ceiling and floor function
        def ce(x):
            if x%1!=0:
                return x//1+1
            else:
                return x//1

        def fl(x):
            return x//1

        #consider the people in batches aproximately 2**n in each batch
        #all gaps are within 1 of each other.
        #O(ln(n)) time I think, should be sufficient for large.
        #takes advantage of fact that position is not required, just gaps :)

        maxhalf = N
        minhalf = 0
        Nmaxhalf = 1
        Nminhalf = 0
        batches = -1

        done = False
        while done == False:
            batches+=1
            power = 2**batches
            if K>power:
                K-=power
            elif K>Nmaxhalf:
                answer1 = ce((minhalf-1)/2)
                answer2 = fl((minhalf-1)/2)
                done = True
            else:
                answer1 = ce((maxhalf-1)/2)
                answer2 = fl((maxhalf-1)/2)
                done = True

            if Nminhalf!=0:
                newmaxhalf = ce((maxhalf-1)/2)
                newminhalf = fl((minhalf-1)/2)
                if minhalf%2==0:
                    newNminhalf = Nminhalf
                    newNmaxhalf = 2*Nmaxhalf + Nminhalf
                else:
                    newNminhalf = 2*Nminhalf + Nmaxhalf
                    newNmaxhalf = Nmaxhalf
            elif int(maxhalf)%2==0:
                newNmaxhalf = Nmaxhalf
                newNminhalf = Nmaxhalf
                newmaxhalf = maxhalf/2
                newminhalf = (maxhalf-1)/2
            else:
                newNmaxhalf = 2*Nmaxhalf
                newNminhalf = 0
                newmaxhalf = (maxhalf-1)/2
                newminhalf = 0
            maxhalf = newmaxhalf
            minhalf = newminhalf
            Nmaxhalf = newNmaxhalf
            Nminhalf = newNminhalf #the batch has went in

        print("Case #"+str(case)+": "+ str(int(answer1))+ " " + str(int(answer2)))




