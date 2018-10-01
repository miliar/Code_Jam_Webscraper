o = open("q3.output", 'r+')

cnt = 1

with open ("q3.input") as f:
    # read the fistline as the T
    T = f.readline()
    print 'No of test cases:', T,

    while True:
        t_case = f.readline()
        if not t_case:
            print "-- End of file"
            break

        output = 0
        cl = list()

        case_list = t_case.split()
        A = long(case_list[0])
        B = long(case_list[1])+1

        for W in range(A, B):
            cW = list(str(W))

            if len(cW) == 1:
                continue

            len_cnt = len(cW)-1

            while True:
                if len_cnt == 0:
                    break

                in_list = 0

                W1 = cW.pop()
                cW.insert(0, W1)

                nW = "".join(cW)

                if long(nW)>=A and long(nW)<B and long(nW) > long(W):
                    for l in range(len(cl)):
                        if cl[l][0] == long(W) and cl[l][1] == long(nW):
                            in_list = 1
                            break

                    if in_list == 0:
                        cl.append([long(W), long(nW)])
                        output += 1

                len_cnt -= 1


        print len(cl)


        # result
        o.write('Case #')
        o.write(str(cnt))
        o.write(': ')
        o.write(str(output))
        o.write('\n')
        cnt += 1

o.close()
