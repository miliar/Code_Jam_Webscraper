import tkFileDialog
import sys

def main():
    infile = (len(sys.argv) > 1 and sys.argv[1]) or tkFileDialog.askopenfilename(title="Select input file", initialdir='.', filetypes = [('Input','.in')])
    outfile = infile.replace(".in", ".out", 1);
    print "Output file will be: %s" % outfile
    with open(infile, "r") as f:
        lines = f.readlines()
    of = open(outfile, "w")
    print int(lines[0])
    counter = 1;
    for line in lines[1:]:
        lastPosB = 1
        lastPosO = 1
        lastTimeB = 0
        lastTimeO = 0
        print line.split()[1:]
        i = iter(line.split()[1:])
        while 1:
            try:
                colour = i.next()
                newPos = int(i.next())
                if colour == 'B':
                    lastTimeB = max(lastTimeB + abs(newPos - lastPosB) + 1, lastTimeO + 1)
                    lastPosB = newPos
                    print "B push %d: %d" % (newPos, lastTimeB)
                if colour == 'O':
                    lastTimeO = max(lastTimeO + abs(newPos - lastPosO) + 1, lastTimeB + 1)
                    lastPosO = newPos
                    print "O push %d: %d " % (newPos, lastTimeO)
            except StopIteration:
                answer = max(lastTimeB, lastTimeO)
                print answer
                of.write("Case #%d: %d\n" % (counter, answer))
                counter += 1
                break
    of.close()
        
if __name__ == '__main__':
    main()