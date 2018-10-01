'''
Created on 14 Apr 2012

@author: oracal
'''
import string
def main():
    
    mapping = {}
    mapping['y']='a'
    mapping['e'] = 'o'
    mapping['q'] = 'z'
    example = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

    example_output = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

    for letter,output_letter in zip(example,example_output):
        if letter ==' ' or letter == '\n':
            continue
        else:
            mapping[letter] = output_letter
    
    example_letters = string.ascii_lowercase
    output_letters = list(string.ascii_lowercase)
    if len(mapping) <26 and len(mapping) > 24:
    
        for letter in example_letters:
            if letter in mapping:
                output_letters.remove(mapping[letter])
            else:
                x = letter
        mapping[x] = output_letters[0]
#    print mapping
#    for key,value in sorted(mapping.iteritems(),key=lambda (k,y): y):
#        print key + ':' + value
    output_list =[]
    with open('A-small-attempt0.in') as f:
        f.next()
        for line in f:
            line_output = ''
            for letter in line:
                if letter ==' ' or letter == '\n':
                    line_output += letter
                else:
                    line_output += mapping[letter]
            output_list.append(line_output)
    with open('output.txt', 'w') as o:
        for count,output in enumerate(output_list,start=1):
            o.write('Case #%s: %s' % (count,output))
        
        
                    
    

if __name__ == '__main__':
    main()