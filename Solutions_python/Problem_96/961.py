
def figure_out_scores(score, p):
    if score < p:
        return 0
    if score >= max(0,3*p-4):
        if score >= 3*p-2:
            return 1 #at least p and not surprising
        else:
            return 2 #at least p but surprising

    else:
        return 0 # maximum score below p

def dance(filename, output_tag):
    f = open(filename, 'r')
    output= open(output_tag+'_output.txt','w')
    num_of_case = int(f.readline())
    for caseid in range(num_of_case):
        flag_debug = False
        if flag_debug:
            if caseid ==2:
                print 'break'
        record = f.readline().split('\n')[0].split()
        record = [int(integer) for integer in record]
#        print record
        num_of_scores = record[0]
        num_of_allowed_surprise = record[1]
        p = record[2]
        scores = record[3:]
        num_of_non_surprise = 0
        num_of_surprise = 0
        for sid in range(num_of_scores):
            mark = figure_out_scores(scores[sid],p)
            if mark == 1:
                num_of_non_surprise += 1
            if mark == 2:
                num_of_surprise += 1

        maximum_number = num_of_non_surprise + min(num_of_allowed_surprise, num_of_surprise)
#        print maximum_number


        output.write('Case #'+str(caseid+1)+': '+str(maximum_number)+'\n')

    f.close()
    output.close()

if __name__ == '__main__':
    dance('B-large.in', 'dance_large')
  