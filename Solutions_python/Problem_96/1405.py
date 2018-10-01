'''
Created on Apr 13, 2012

@author: redoacs
'''


input = 'B-large.in'
output = 'B-large.out'

if __name__ == '__main__':
    input_file = open(input)
    output_file = open(output, 'w')
    ntc = int(input_file.readline());
    
    for i in range(ntc):
        tc = input_file.readline().split()
        #print(tc)
        n = int(tc[0])
        s = int(tc[1])
        p = int(tc[2])
        total_scores = [int(score_str) for score_str in tc[3:]]
        #print(n, s, p, total_scores)
        sc = 0;
        nvc = 0;
        for total in total_scores:
            sub_total = total - p
            #print('total', total, '| sub_total', sub_total, max([0,(p-2)*2]), max([0,(p-1)*2]) )
            if ( sub_total < max([0,(p-2)*2]) ):
                nvc += 1
            else: 
                if (sub_total < max([0,(p-1)*2]) ):
                    sc += 1
        nvs = max([0,sc-s]) 
        #print('nvc', nvc , '| sc', sc, '| nvs', nvs)
        
        print('Case #', i+1 , ": " , n-nvc-nvs, sep='')
        print('Case #', i+1 , ": " , n-nvc-nvs, sep='', file=output_file)