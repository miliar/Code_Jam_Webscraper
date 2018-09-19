import sys

if not len(sys.argv) == 3:
    exit("""Wrong usage parameters supplied!
    
    Usage:
    %s input output""" % __file__
    )

POSSIBLE_RESULT = "Possible"
BROKEN_RESULT = "Broken"

def get_letter_positions(word, letter):
    pos = []
    for i in xrange(len(word)):
        if word[i] == letter:
            pos.append(i)
    return pos
    
def filter_list(sean_list, l):
    filtered = []
    for w in sean_list:
        if len(w) == l:
            filtered.append(w)
    return filtered

def filter_list_by_letter(sean_list, word, letter):
    filtered = []
    ok_pos = get_letter_positions(word, letter)
    for w in sean_list:
        if get_letter_positions(w, letter) == ok_pos:
            filtered.append(w)
            
    return filtered

def is_letter_in_any_word(sean_list, letter):
    for w in sean_list:
        if letter in w:
            return True
    return False

def get_points(sean_list, word, li):
    l = len(word)
    sean_list = filter_list(sean_list, l)
    p = 0
    k = 0
    guessed = []
    wordk = 0
    while len(sean_list) > 1:
        letter = li[k]
        
        if is_letter_in_any_word(sean_list, letter):
            if not get_letter_positions(word, letter):
                p += 1
            sean_list = filter_list_by_letter(sean_list, word, letter)
        k += 1
    return p
           
    
def get_killer_word(d, li):
    points = (0, d[0], 0)
    for i in xrange(len(d)):
        sean_list = d[:]
        pwordi = get_points(sean_list, d[i], li)
        if pwordi > points[2]:
            points = (i, d[i], pwordi)
    return (points[0], points[1])
    
def solve(m, d, l):
    words = []
    for i in xrange(m):
        killer_word = get_killer_word(d, l[i])
        words.append(killer_word[1])
    return words
    
def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):
            
            (n, m) = [int(x) for x in input_f.readline().split(" ")]
            d = []
            for i in xrange(n):
                d.append(input_f.readline().strip())
            l = []
            for i in xrange(m):
                l.append(input_f.readline().strip())
                
            result = solve(m, d, l)
            
            output_f.write("Case #%d: %s\n" % (test_case_i + 1, " ".join(result)))
    
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])
