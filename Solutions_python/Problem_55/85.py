import subprocess,time

if __name__ == "__main__":
    T = int(raw_input())
    cases = {}
    unsolved = set(range(1,T+1))
    for i in range(1, T+1):
        R,k,N = map(int, raw_input().split())
        groups = raw_input().strip()
        cases[i] = (R,k,N,groups)

    running = {}
    while unsolved or running:
        if len(running) == 2 or not unsolved:
            time.sleep(0.1)
            for key,val in running.items():
                retcode = val.poll()
                if retcode is None:
                    continue
                cases[key] = val.stdout.read().strip()
                del(running[key])

        else:
            a = unsolved.pop()
            f = open('%d.tmp'% a, 'w')
            f.write("%d %d %d\n" % cases[a][:3])
            f.write("%s\n" % cases[a][3])
            f.flush()
            f.close()
            running[a] = subprocess.Popen(('/usr/bin/python', 'coaster.py', '%d.tmp' % a), stdout = subprocess.PIPE)
        
    for i in range(1, T+1):
        print "Case #%d: %s" % (i, cases[i])
