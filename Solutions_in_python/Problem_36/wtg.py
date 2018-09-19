search_string = "welcome to code jam"
search_string_len = len(search_string)
tested_matches = []

def findMatch(search_string, text):
    match = {}
    for search_string_index in xrange(len(search_string)):
        try:
            if search_string_index == 0:
                match[search_string_index] = text.index(search_string[search_string_index])
            else:
                match[search_string_index] = text[match[search_string_index - 1]:].index(search_string[search_string_index]) + match[search_string_index - 1]
        except:
            return None
    
    return match

def is_match(match, indata):
    if match in tested_matches:
        return False

    tested_matches.append(match)
    
    is_matching = True
    
    for k,v in match.items():
        try:
            if indata[v] != search_string[k]:
                is_matching = False
        except IndexError,e:
            is_matching = False
            break
            
    return is_matching

def countMatches(match, indata):
    indata_length = len(indata)
    num_matches = 0
    if is_match(match, indata):
        num_matches += 1

    for k,v in reversed(match.items()):
        temp_match = match.copy()
        next_match = None
        try:
            next_match = indata[v+1:].index(indata[v])
        except ValueError:
            pass

        if next_match == None:
            pass
        else:
            if (temp_match.has_key(k+1) and temp_match[k+1] >= v+1+next_match) or not temp_match.has_key(k+1):
                temp_match[k] = v+1+next_match
                if temp_match not in tested_matches:
                    num_matches += countMatches(temp_match, indata)

    return num_matches

for case in xrange(input()):
    tested_matches = []
    indata = raw_input()
    matches = 0

    match = findMatch(search_string,indata)
    if match:
        matches = countMatches(match, indata)

    matches_string = "%04i" % matches
    matches_string = matches_string[-4:]
    print "Case #%i: %s" % (case+1, matches_string)

