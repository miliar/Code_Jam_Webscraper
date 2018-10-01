from pylab import *
from fractions import gcd
from scipy.misc import comb, factorial
import re, sys

def handle(infile, outfile):
    line = infile.readline().split();
    n, pd, pg = [int(x) for x in line];
    if (pd > 0 and pg == 0) or (pd < 100 and pg == 100):
        s = "Broken";
    else:
        wd = int(pd * n / 100.0);
        d = pd / gcd(pd, 100);
        g = pg / gcd(pg, 100);
        if d <= wd:
            s = "Possible";
        else:
            s = "Broken";
    outfile.write(' %s' % s);

if len(sys.argv) != 2: exit();
infile = file(sys.argv[1] + '.in', 'r');
outfile = file(sys.argv[1] + '.out', 'w');

count = int(infile.readline());
for i in range(count):
    print 'Case #%d' % (i + 1);
    outfile.write('Case #%d:' % (i + 1));
    result = handle(infile, outfile);
    outfile.write('\n');
