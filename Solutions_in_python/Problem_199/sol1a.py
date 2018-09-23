
kitchen = []

with open("input.txt") as f:
    file_o = open('output.txt','w') #GET IT OPEN HERE
    input = f.readlines()
    input_x = [i.replace("\n", "") for i in input]
    test_size = int( input_x[0] )

    if test_size == len(input_x[1:]):

        for j in range(0, test_size):
            kitchen.append(input_x[j+1].split(" "))

            # THE FUN BEGINS
            cakes_in = [kitchen[j][0][i] for i in range(0,len(kitchen[j][0]))] # array of initial state
            k = int( kitchen[j][1] ) # size of the flipper

            print("test ",cakes_in, k, len(cakes_in))

            aux = []
            index = 0
            cakes_out = [None] * len(cakes_in)
            shadow = []
            flips = 0
            flag = False

            while index < len(cakes_in):

                # Go through the array until '-' shows up
                try:
                    while (cakes_in[index] == '+'):
                        index+=1
                        #cakes_out[:index] = '+'

                except:
                    print('finished array')
                    index = len(cakes_in) + 1
                    break

                print(index)
                #  The first if signals that we may be in trouble, because the
                #  number of cakes left is less than K
                if len(cakes_in) - index < k:
                    if '-' in cakes_in[index:]:
                        flag = True
                        break
                    for d in range(index, len(cakes_in)):
                        aux.append(cakes_in[d])
                else:
                    for d in range(index, index + k):
                        aux.append(cakes_in[d])
                    #index+= k
                print (aux)
                # HERE WE FLIP, but only if we have enough cakes
                if len(aux) == k and aux.count('+') != k:
                    flips += 1
                    for p in range(0, len(aux)):
                        if aux[p] == '-':
                            aux[p] = '+'
                        elif aux[p] == '+':
                            aux[p] = '-'
                print(aux)


                cakes_in[index : index+k] = aux[0:k]
                print (cakes_in)

                aux = []
                index = 0

            print ("result: ", cakes_in, flips)
            if (not flag):
                file_o.write("Case #"+ str(j+1) +": "+ str(flips)+"\n")
            elif (flag):
                file_o.write("Case #"+ str(j+1)+": IMPOSSIBLE\n")


    else:
        print ("Size Error!")
    file_o.close()
