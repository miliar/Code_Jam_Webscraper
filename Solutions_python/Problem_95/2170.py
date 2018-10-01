from string import maketrans, translate

INPUT_FILE = 'A-small-attempt0.in'
OUTPUT_FILE = INPUT_FILE + '.out.txt'


def learn():
    # learn language from example text (and don't forget the hint)
    input  = 'q aoz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
    output = 'z yeq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

    # check if all characters are covered
    for x in xrange(ord('a'), ord('z')+1):
        if chr(x) not in input:
            print 'Input error', chr(x)
        if chr(x) not in output:
            print 'Output error', chr(x)
    return maketrans(input, output)
    
    
if __name__ == '__main__':
    table = learn()
   
    #read all input lines
    f = open(INPUT_FILE, 'r')
    data = f.readlines()
    f.close()

    #how many test cases
    T = int(data[0])

    #run all test cases
    f = open(OUTPUT_FILE, 'w')
    for i, t in enumerate(data[1:]):
        f.write('Case #%d: %s' % (i+1, translate(t, table)))
    f.close()
    