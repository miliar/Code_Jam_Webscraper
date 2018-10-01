def robots(z):
    step = 0
    positions = {'B':1,'O':1}
    directions = {'B':0,'O':0}
    while z:
        active, target = z[0]
        inactive = 'B' if active == 'O' else 'O'
        next = lookup(inactive, z)
        directions[active] = target - positions[active]
        if next:
            directions[inactive] = next - positions[inactive]
        #print directions,positions,z
        if directions[active] != 0:
            positions[active] += 2*(directions[active] > 0)-1
        else:
            z = z[1:]
        if directions[inactive] != 0:
            positions[inactive] += 2*(directions[inactive] > 0)-1
        step += 1
        #raw_input()
    return step
        
        
        
def lookup(key, z):
    for r,i in z:
        if key == r:
            return i
            
def test():             
    print robots([('O', 2), ('B' ,1) ,('B' ,2),('O', 4)])
    
def main():
    cases = int(raw_input())
    for case in range(cases):
         m = raw_input().split(" ")
         m = [(m[2*i+1],int(m[2*i+2])) for i in range(int(m[0]))]
         print "Case #%d: %d" % (case+1, robots(m))

main()
