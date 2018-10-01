import itertools 

def game(old, new, catalina):

    #generate three arrays for each input that will contain all non-negative 
    #numbers less than current input number

    olds = [i for i in range(old)]
    news = [i for i in range(new)]
    catalinas = [i for i in range(catalina)]

    possiblities = list(itertools.product(olds, news))

    

    # possiblities1 = list(itertools.product(olds, catalinas))
    # possiblities2 = list(itertools.product(news, catalinas))

    # print possiblities1
    # print possiblities2
    # print possiblities

    #iterate over all possiblities and check if both of numbers in each pair
    #exists in catalinas numbers

    count = 0

    for pair in possiblities:
        if pair[0]&pair[1] in catalinas:
            count += 1

    
    return count
    




if __name__ == '__main__':
    
    f = open('B-small-attempt0.in', 'rb')

    lines = f.readlines()
    cases = int(lines[0])
    results = []
    
    for line in lines[1:]:
        old, new, catalina = line.rstrip().split(' ')
        result = game(int(old), int(new), int(catalina))
        results.append(result)

    
    #write down the results to file
    output = open('outputBig.in', 'wb')

    for i in range(cases):
        a = 'Case #' + str(i+1) + ': ' + str(results[i])
        
        output.write(a + '\n')

    output.close()
    # (game(7, 8, 5))
    # print 
    # print 
    # game(3, 4, 2)
    
