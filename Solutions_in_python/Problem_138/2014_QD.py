import sys

def initialize():
    file_in = 'D:\code jam\input.in'
    file_out = 'D:\code jam\output.txt'
    
    try:
        data_in  = open(file_in, 'r')
    except:
        print("Can't open file \'" + data_in +"\'")
        sys.exit()
    
    try:
        data_out  = open(file_out, 'w')
    except:
        print("Can't write to file \'" + data_out +"\'")
        sys.exit()

    return(data_in, data_out)

def get_variables():

    line = data_in.readline().split(' ')
    N = int(line[0])
    

    line = data_in.readline().split(' ')
    naomi=[]
    for i in range(N):
        naomi.append( float(line[i]) )



    line = data_in.readline().split(' ')
    ken=[]
    for i in range(N):
        ken.append( float(line[i]) )

#    print('naomi:', naomi)
    naomi.sort(reverse=True)
#    print('naomi:', naomi)

#    print('ken:', ken)
    ken.sort()
#    print('ken:', ken)

#    print('sizes:', sizes)
#    print('l:', l)
#    print('points_list:', points_list)
    return(naomi,ken)


def calculate_result(naomi,ken):
    deceit=0
    war=0
    
    nao=naomi[:]
    ke=ken[:]
    
#    print('nao:', nao)
#   print('nao:', len(nao))

#DECEIT
    while len(nao):
        test_k = ke.pop()
        if nao[-1] > test_k :
            deceit += len(nao)
            break
            
        if nao[0] > test_k :
            nao.pop(0)
            deceit+=1
        else:
            nao.pop()

#WAR - ken plays optimally
    while len(naomi):
        flag=0
        test_n = naomi.pop()
        for i in range(len(ken)):
            if ken[i] > test_n:
                ken.pop(i)
                flag=1
                break
        if flag==0:
            war = len(naomi) +1
            break

    
    
#    
    result = str(deceit) + ' ' + str(war)
    return result



(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    (naomi,ken) = get_variables()
    if(i==4):
        j=i
#        help('str')
    result = calculate_result(naomi,ken)
    print( 'Case #' + str(i) + ': ' + str(result) )
    data_out.write( 'Case #' + str(i) + ': ' + str(result) + '\n' )
    


