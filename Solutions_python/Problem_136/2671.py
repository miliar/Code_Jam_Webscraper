def parse_in(f):
    lines = open(f,'r').readlines()
    for l in lines[1:]:
        yield map(float,l.split())

def build(c,f,x):
    rate = 2
    buildtime = 0
    while True:
        completetime = x / rate
        yield completetime + buildtime
        buildtime += c / rate
        rate += f

caseno = 1
out = open('/home/toon/Code/codejam/ans.out','w')
def answercase(time):
    global caseno
    out.write("Case #{}: {}\n".format(caseno,time))
    caseno += 1

if __name__ == "__main__":
    for c,f,x in parse_in("/home/toon/Downloads/B-large.in"):
        last = None
        for answer in build(c,f,x):
            if not last or last > answer:
                last = answer
            elif answer > last:
                answercase(last)
                break


