fin = open("recycle.txt")
fin = fin.readlines()

inputs = int(fin[0])

fin.pop(0)

for inp in xrange(inputs):
    case = fin[inp].split(' ')
    low = int(case[0])
    high = int(case[1])

    recycled_pairs = 0
    
    for i in xrange(low, high+1):
        cur_n = str(i)

        prev_m = []
        
        for j in xrange(1, len(cur_n)):
            cur_m = cur_n[j:len(cur_n)] + cur_n[0:j]

            if int(cur_m) >= low and int(cur_m) <= high and\
                    int(cur_n) < int(cur_m) and\
                    int(cur_m) not in prev_m:

                recycled_pairs += 1
                prev_m.append(int(cur_m))
                
    print ("Case #%d: " % (inp + 1)) + str(recycled_pairs)


