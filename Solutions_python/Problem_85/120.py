import tkFileDialog
import sys

def main():
    infile = (len(sys.argv) > 1 and sys.argv[1]) or tkFileDialog.askopenfilename(title="Select input file", initialdir='.', filetypes = [('Input','.in')])
    outfile = infile.replace(".in", ".out", 1);
    print "Output file will be: %s" % outfile
    of = open(outfile, "w")
    with open(infile, "r") as f:
        line = f.readline()
        noCases = int(line)
        print "Number of test cases: %d" % noCases 
        caseNo = 1
        while caseNo <= noCases:
            line = f.readline()
            input = [long(x) for x in line.split()]
            (L, t, N, C) = input[:4]
            dist = input[4:]
            print "Case #%d" % caseNo
            print("L, t, N, C: %d, %d, %d, %d" % (L, t, N, C))
            print("dist: %s" % dist)
            time = long(0)
            boostready = False
            numbers = []
            for i in range(N):
                if boostready:
                    numbers.append(dist[i % C])
                else:
                    if time + 2 * dist[i % C] > t:
                        boostready = True
                        numbers.append(((time + 2 * dist[i % C]) - t) / 2)
                    else:
                        time += 2 * dist[i % C]
            print numbers
            print (time, t)
            numbers.sort(reverse=True)
            print numbers
            if boostready:
                output = sum(numbers[L:]) * 2 + sum(numbers[:L]) + long(t)
            else:
                output = time
            print "Output: %d" % output
            of.write("Case #%d: %s\n" % (caseNo, output))
            caseNo += 1
    of.close()
        
if __name__ == '__main__':
    main()