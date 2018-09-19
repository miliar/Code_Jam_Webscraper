# developped under python3.2
def cal_wp(data, tabou):
    wp = 0
    count_win = 0
    count_loss = 0
    for idx_column in range(0, len(data)):
        if( idx_column != tabou ):
            x = data[idx_column]
            if( x == '1' ):
                count_win += 1
            elif( x == '0' ):
                count_loss += 1
    if( count_win + count_loss == 0 ):
        return 0
    wp = count_win / (count_win + count_loss)
    return wp
def cal_owp(data, data_all, idx_line):
    owp = 0
    count, total = 0, 0
    for idx_column in range(0, len(data)):
        x = data[idx_column]
        if( x=='1' or x=='0' ):
            total += cal_wp(data_all[idx_column], idx_line)
            count += 1
    if( count == 0):
        return 0
    owp = total / count
    return owp
def cal_oowp(data, owp):
    oowp = 0
    count, total = 0, 0
    for idx_column in range(0, len(data)):
        x = data[idx_column]
        if( x=='1' or x=='0' ):
            total += owp[idx_column]
            count += 1
    if( count == 0):
        return 0
    oowp = total / count
    return oowp
# test_file_name = 'A-test'
test_file_name = 'A-large'
f = open(test_file_name + '.in', 'r')
fw = open(test_file_name + '.out', 'w')
T = int(f.readline())
for case in range(1,T+1):
    #print(i)
    
    line = f.readline()
    line = line.split()
    line.reverse()

    # count of elements
    N = int(line.pop())

    # read data
    wp, owp, oowp = [], [], []   # values
    scores = []
    data = [];
    
    for idx_line in range(0, N):
        line = f.readline()
        line = list(line)
        line.reverse()

        data_line = [];

        for idx_column in range(0, N):
            data_line.append( line.pop() )

        data.append( data_line )

    # end read data

    # data process
    for idx_line in range(0,N):
        wp.append( cal_wp(data[idx_line], None ) )
#     print(wp)
    for idx_line in range(0,N):
        owp.append( cal_owp(data[idx_line], data, idx_line) )
#     print(owp)
    for idx_line in range(0,N):
        oowp.append( cal_oowp(data[idx_line], owp) )
#     print(oowp)

    for element in range(0,N):
        score = 0.25*wp[element] + 0.5*owp[element] + 0.25*oowp[element]
#         print(score)
        scores.append( score )
            
    # end data process

    # result representation
    ans = ""
    for element in scores:
        ans += str(element) + '\n'
        
    #print(ans)
    output = 'Case #' + str(case) +': \n' + str(ans)
    print(output)

    fw.write(output)

    # end result representation

f.close()
fw.close()
