from sys import argv, stdout



def main():
    input_file = argv[1]
    output_file = argv[2]

    with open(input_file,'r') as fin:
        with open(output_file,'w') as fout:
            num = int(fin.readline().strip())
            testcase = 1
            for line in fin:
                if line[0] == '#':
                    continue
                line = line.strip()
                splits = line.split(' ')
                max_shy = int(splits[0])

                standing = 0
                friends = 0
                for i, c in enumerate(splits[1]):
                    amount = int(c)
                    # print 'Level %d Standing %d Friends %d Amount %d' % (i, standing, friends, amount)
                    if standing >= i:
                        # print 'Level passed'
                        standing += amount
                    else:
                        # print 'Insufficient, adding %d friends' % (i - standing)
                        additional = i - standing
                        friends += additional
                        standing += additional + amount

                fout.write('Case #%d: %s\n' % (testcase, friends))
                testcase += 1



if __name__ == '__main__':
    main()



