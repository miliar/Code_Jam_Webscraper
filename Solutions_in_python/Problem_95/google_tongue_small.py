def convert_sentence(sentence):
    
    new_sentence = ""
    for char in sentence:
        if char in trans_dict:
            char = trans_dict[char]
        new_sentence += char
        
    return new_sentence
    
trans_dict = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's',
              'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i',
              'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',
              'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j',
              't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

pagename = "A-small-attempt.in"
page = open(pagename, "r")
number_of_tests = int(page.readline().strip())
answer_pagename = "google_tongue_small_output.in"
answer_page = open(answer_pagename, "w")

for i in range(1, number_of_tests + 1):
    sentence = page.readline().strip()
    answer_page.write("Case #%d: %s\n" % (i, convert_sentence(sentence)))