from collections import defaultdict

def inc_in_dict(d, l, c):
    d[l]+=c

def solve(l,k):
    places = defaultdict(int)
    places[l] = 1
    while k:
        (l1, c) = max(places.items())
        del places[l1]
        l2 = l1//2
        l3 = max(((l1-1)//2),0)
        if c >= k:
            return "{} {}".format(l2, l3)
        k -= c
        inc_in_dict(places, l2, c)
        inc_in_dict(places, l3, c)
        
            


with open("C-large.in", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = lines[0]
    for i in range(1, len(lines)):
        [L,K] = lines[i].split(" ")
        ofile.write("Case #{}: {}\n".format(i, solve(int(L), int(K))))