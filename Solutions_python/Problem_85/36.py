
def solve(case):
    int_input = map(int,raw_input().split());
    (l,t,n,c) = int_input[0:4]

    tdl = list(map(lambda x: x*2,int_input[4:]))
    dl=[]
    while len(dl) < n:
        dl.extend(tdl)
    del(dl[n:])
            
    start_pos_list=[0]
    start_pos = 0
    for d in dl:
        start_pos = start_pos + d
        start_pos_list.append(start_pos)
    odl = zip(dl,range(n))
    odl.sort()
    odl.reverse()

#    print dl
#    print start_pos_list
#    print odl

    t_off = 0
    for off in range(n):
        t_off = off
        if start_pos_list[off+1]>=t:
            break

    t_gain = (start_pos_list[t_off+1]-t)/2
#    print "t_off=%s" % t_off
#    print "t_gain=%s" % t_gain

    t_gain_used = False

    i = 0
    total_gain = 0
    while i < len(odl) and l > 0:
        d, off = odl[i]
        if off <= t_off:
            i = i+1
            continue
        else:
            gain = d/2
            if not t_gain_used and gain < t_gain:
                t_gain_used = True
                total_gain = total_gain + t_gain
                l = l-1
                continue
            else:
                total_gain = total_gain + gain
                l = l-1
                i = i+1
                continue

    if not t_gain_used and l > 0:
        total_gain = total_gain + t_gain

    print "Case #%s: %s" % (case, start_pos_list[n]-total_gain)

def main():
    t = int(raw_input())
    for i in range(t):
        solve(i+1)

main()
