def read_input():
    first_an=input()
    a=[]
    a.append(raw_input().split()[0:])
    a.append(raw_input().split()[0:])
    a.append(raw_input().split()[0:])
    a.append(raw_input().split()[0:])

    sec_an=input()

    b=[]
    b.append(raw_input().split()[0:])
    b.append(raw_input().split()[0:])
    b.append(raw_input().split()[0:])
    b.append(raw_input().split()[0:])

    vals=(set(a[int(first_an)-1]) & set(b[int(sec_an)-1]))


    if len(vals)==1:
        return vals.pop()
    if len(vals)==0:
        return "Volunteer cheated!"
    if len(vals)>1:
        return "Bad magician!"



def run_command():
    pass

numCases=input()
for i in range(1, numCases+1):
    #read_input()
    output = read_input()
    print "Case #%d:" % i, output
