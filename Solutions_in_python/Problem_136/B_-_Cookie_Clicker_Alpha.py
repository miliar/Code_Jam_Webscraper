import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        
        line = sys.stdin.readline()
        C, F, X = map(float,line.split())
        #print C, F, X
        #C : Cookies to buy a farm
        #F : Extra cookies for each farm
        #X : How many cookies I need to win
        
        cookie_prod = 2.0
        new_time = X / cookie_prod
        min_time = float('inf')
        nb_farm = 1
        
        tot = C / cookie_prod
        while new_time < min_time:
            min_time = new_time
            #print '\t', new_time, tot, nb_farm
            
            new_time = tot + X / (nb_farm*F + cookie_prod)
            tot += C / ( 2.0 + F*(nb_farm) )
            nb_farm += 1
            
             
        print 'Case #%d: %.7f' %(case, min_time)   
            
        
main()

'''
Input

4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

  	
Output	

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762

'''
