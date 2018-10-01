import sys

cache = {}

def search(source, word):
    global cache
    if (source, word) in cache:
        return cache[(source,word)]
    
    result = 0
    srclen = len(source)
    
    for i in range(srclen):
        if source[i] == word[0]:
            if len(word) == 1:
                result += 1
            elif i != srclen - 1:
                result += search(source[i+1:], word[1:])
                
    cache[(source,word)] = result
    return result


def main():
    global cache
    input = open(sys.argv[1])
    num_cases = int(input.readline())
    
    for n in range(1, num_cases+1):
        cache = {}
        answer = str(search(input.readline().strip(), 'welcome to code jam'))
        output = answer[-4:].zfill(4)
        print 'Case #%d: %s' % (n, output)
        

if __name__ == '__main__':
    main()
    
