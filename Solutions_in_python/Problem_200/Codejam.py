f = open("B-large.in")
o = open("outputL.txt","w")
no_of_cases = f.readline()


def check_inc(num):
    no = list(str(num))
    for i in range(len(no)-1):
        if no[i]>no[i+1]:
            return int(''.join(no[i+1:]))+1
    return 0

for i in range(int(no_of_cases)):
    number = int(f.readline())
    no = 1
    while no:
        no = check_inc(number)
        number -= no
    o.write("Case #"+str(i+1)+": "+str(number)+"\n")
    