filename = 'A-large.in'

def invite(audi):
    num = 0
    for i in range(1, len(audi)):
        num += max(0, i - sum(audi[0:i]) - num)
    return num

out = open('Aoutput_large.txt', 'w');
with open(filename, 'r') as f:
    case = int(f.readline())
    for i in range(0, case):
        part = f.readline().split();
        l = [int(x) for x in part[1]]
        num = invite(l)
        out.write('Case #' + str(i+1) + ': ' + str(num) + '\n')
    out.close()
f.close()