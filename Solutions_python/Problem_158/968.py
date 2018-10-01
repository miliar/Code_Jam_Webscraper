if __name__ == "__main__":
    fin = open('D-small-attempt4.in', 'r')
    fout = open('D-small-attempt4.out', 'w')

    #fin = open('t.in', 'r')
    #fout = open('t.out', 'w')

    cases = fin.readline()
    #print cases

    for case_num in range(0, int(cases)):
        line = fin.readline().split(' ')
        print line
        winner = "GABRIEL"

        x = int(line[0])
        r = int(line[1])
        c = int(line[2])

        if x == 1:
            winner = "GABRIEL"
        elif x > 6:
            winner = "RICHARD"
        elif x > max(r, c):
            winner = "RICHARD"
        elif (r*c) % x != 0:
            winner = "RICHARD"
        elif (x - min(r, c)) > min(r, c):
            winner = "RICHARD"
        elif ((x-min(r, c)) >= (min(r, c))) & (min(r, c) >= 2):
            winner = "RICHARD"

        print "Case #" + str(case_num+1) + ": " + winner
        #if winner != line[3].replace('\n', ''):
        #    print "WHAAAAAAAAAAAAAAAT"
        fout.write("Case #" + str(case_num + 1) + ": " + winner + "\n")

    fin.close()
    fout.close()