def xor(z):
    return reduce(lambda a,b:a^b, z, 0)
    
def split(z):
    if xor(z) == 0:
        return str(sum(z) - min(z))
    else:
        return "NO"

def main():
    cases = int(raw_input())
    for case in range(cases):
        n = raw_input()
        z = map(int, raw_input().split(" "))
        print "Case #%d: %s" % (case+1, split(z))

main()
