# Code Jam Round 2
# 13/9/2009

inname = 'E:\A.in.txt'

fin = open(inname, 'r')
fout = open('E:\A.out.txt', 'w')

lines = fin.readlines()

cases = int(lines[0].strip())

i = 1
for l in lines[1:]:
    what = l.strip()
    mapp = {}
    if len(what) == 1:
        fout.write('Case #' + str(i) + ': ' + str(1) + '\n')
    else:
        mapp[what[0]] = 1
        current = 0
        for c in what[1:]:
            if not c in mapp:
                mapp[c] = current
                if current == 0:
                    current = 2
                else:
                    current += 1
        min_base = max(2, len(mapp))
        answer = 0
        j = 1
        for c in range(len(what) - 1, -1, -1):
            answer += mapp[what[c]] * j
            j *= min_base
        fout.write('Case #' + str(i) + ': ' + str(answer) + '\n')
    i += 1    

fout.close()
fin.close()   
    
