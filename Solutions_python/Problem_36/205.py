import sys
import re

string = 'welcome to code jam'
pattern = 'acdejlmotw '

for n in range(int(sys.stdin.readline())):
    text = re.sub('[^%s]'%pattern, '', sys.stdin.readline())
    
    def count_matches(string, text):
        result = 0
        
        # Find each group separated by next letter
        if len(string) > 1:
            pattern = '%s[^%s]*' % tuple(string[1::-1])

            match = re.search(pattern, text)
            while match:
                count = len(re.findall(string[0], text[:match.start()]))
                if count > 0:
                    result += ( count * count_matches(string[1:], text[match.start():]) ) % 10000
                    
                text = text[match.end():]
                match = re.search(pattern, text)
        else:
            result = len(re.findall(string[0], text))
            
        return result

            
    print "Case #%d: %04d" % (n+1, count_matches(string, text))
