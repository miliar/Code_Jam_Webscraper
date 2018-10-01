#!/usr/bin/python

def main():

    T = int(raw_input())

    for i in range(T):

        (max_shyness, audience_string) = raw_input().split(' ')

        max_shyness = int(max_shyness)

        audience_count = list()

        for c in audience_string:
            audience_count.append(int(c))

        cumulative_count = 0
        extra_total = 0

        for j in range(max_shyness):

            cumulative_count += audience_count[j]

            if(cumulative_count >= max_shyness):
                break
            
            if(cumulative_count < j+1):
                extra = ((j + 1) - cumulative_count)
                extra_total += extra 
                cumulative_count += extra

        print "Case #%d: %d" % (i+1, extra_total)

if __name__ == '__main__':
    main()
