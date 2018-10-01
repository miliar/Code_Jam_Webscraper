import fileinput

def binaryseach(num, list, size_of_last):
    sz = len(list)
    id = sz/2
    while True:
        if list[id] < num:
            id = binaryseach(num, list[id:], id + size_of_last)
            return id
        else:
            if sz < 10:
                for i in range(id,sz):
                    if list[i] > num:
                        return size_of_last + i
            else:
                return binaryseach(num, list, id + size_of_last)


def main():
    input = []
    for line in fileinput.input():
        input.append(line)

    numcases = int(input[0])

    for i in xrange(numcases):
        #numblocks = int(input[i *3 +1])
        naomi_blocks = [float(num) for num in input[i * 3 + 2].split()]
        ken_blocks = [float(num) for num in input[i * 3 + 3].split()]
        fsorted_n = sorted(naomi_blocks)
        fsorted_k = sorted(ken_blocks)
        #rsorted_n = sorted(naomi_blocks, reverse=True)
        rsorted_k = sorted(ken_blocks, reverse=True)
        optimalscore, score = 0,0
        # for i in range(numblocks):
         #    if fsorted_n[i] > rsorted_k[i]:
          #       optimalscore += 1
        for num in rsorted_k:
            if num < fsorted_n[len(fsorted_n)-1]:
                for j in range(len(fsorted_n)):
                    if fsorted_n[j] > num:
                        del fsorted_n[j]
                        break
                #index = binaryseach(num, fsorted_n,0)
                #del fsorted_n[index]
                optimalscore+= 1
            else:
                del fsorted_n[0]
        for num in naomi_blocks:
            if num < fsorted_k[len(fsorted_k)-1]:
                for j in range(len(fsorted_k)):
                    if fsorted_k[j] > num:
                        del fsorted_k[j]
                        break
                #index = binaryseach(num, fsorted_k,0)
                #del fsorted_k[index]
            else:
                score += 1
                del fsorted_k[0]

        print "Case #" + str(i + 1) + ":",
        print optimalscore, score



if __name__ == '__main__':
    main()
