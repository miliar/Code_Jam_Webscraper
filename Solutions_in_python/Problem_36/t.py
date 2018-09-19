import subprocess, sys
s = open('/tmp/t.txt', 'r').readlines()
N = int(s[0])
for x, line in enumerate(s[1:]):
    sys.stdout.write("Case #%s: " % (x+1))
    sys.stdout.flush()
    subprocess.Popen(['./a.out','welcome to code jam',line], stdout=sys.stdout).wait()
    sys.stdout.flush()
