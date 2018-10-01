import re

def subregify(subpat):
    return ''.join(['(', '|'.join(subpat[1:-1]), ')'])

def regify(pattern):
    close = pattern.find(')')
    if pattern.startswith('(') and close + 1 <= len(pattern):
        return ''.join([subregify(pattern[0: close + 1]), regify(pattern[close + 1:])])
    elif len(pattern) > 0:
        return ''.join([pattern[0], regify(pattern[1:])])
    else:
        return ''

if __name__=='__main__':

##    print regify('(abc)(def)')
    
    ldn = raw_input().split()
    words = []
    for num_d in range(int(ldn[1])):
        words.append(raw_input().strip())

    for n in range(int(ldn[2])):
        cnt = 0
        pattern = regify(raw_input())
        m = re.compile(pattern)
        for word in words:
            if m.match(word):
                cnt += 1
        print 'Case #%d: %d' % (n + 1, cnt)
    
    
