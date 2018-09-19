
import mpmath;
mpmath.mp.dps=200;

sample_input = """4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0""";

import cStringIO;


#f_in = cStringIO.StringIO(sample_input);
f_in = open("B-large.in", "r");
f_iter = iter(f_in);

T = int(f_iter.next().strip());

for t in range(T):
    C, F, X = map(mpmath.mpf, f_iter.next().strip().split(" "));
    R = mpmath.mpf("2.0");
    t_no_farm = mpmath.mpf(0); 
    t_farm = mpmath.mpf(0);
    time = mpmath.mpf(0);
    
    while True:
        if X <= C:
            time += X/R;
            break;
        
        time += C/R;
        t_no_farm = (X-C)/(R); 
        t_farm = X/(R+F);
        if t_farm < t_no_farm:
            R += F;
        else:
            time += t_no_farm;
            break;
    
    print "Case #%i: %.7f" % (t+1, time);
    
