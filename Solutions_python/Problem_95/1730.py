def create_full_dict(encrypted, decrypted, given):
    d = dict(zip(encrypted, decrypted))
    d.update(given)
    return d

def translate(decrypted, dictionary):
    return ''.join(dictionary[c] for c in decrypted)

def decrypt_file(input_file, googlerese_dict):
    with open(input_file) as f:
        decrypted_lines = [translate(line.strip().rstrip(), googlerese_dict) for 
            line in f.readlines()[1:]]
    return decrypted_lines

def format_output(lines):
    return ''.join('Case #'+str(i)+': ' + line + '\n' 
            for i,line in zip(range(1,len(lines)+1), lines))

encrypted = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
    
decrypted = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

input_file = 'A-small-attempt0.in'
output_file = 'problem_a_output.txt'

if __name__ == '__main__':
    given = {'y':'a', 'e':'o', 'q':'z', 'z':'q'}
    googlerese_dict = create_full_dict(encrypted, decrypted, given)
    decrypted_lines = decrypt_file(input_file, googlerese_dict)
    with open(output_file, 'w') as f: f.write(format_output(decrypted_lines))