import sys
import os

if __name__ == '__main__':

    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        c, f, x = [float(num) for num in sys.stdin.readline().split()]        

        speed = 2.0
        time = 0

        while(x/speed > (x/(speed+f))+c/speed):
            #print speed, time
            time += c/speed
            speed += f
            

        time += x/speed
        sys.stdout.write('Case #{0}: {1}\n'.format(i+1, round(time,7)))       


 
#                    sys.stdout.write('Case #{0}: {1}\n'.format(i+1, "Bad magician!"))

            
                


