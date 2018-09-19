TYPE = "small"

in_file = open("..\\input\\2012-qual-A-%s.txt" % TYPE, "r")
out_file = open("..\\output\\2012-qual-A-%s.txt" % TYPE, "w")

num_cases = int(in_file.readline().strip())

MAPPINGS = {'a' : 'y',
            'b' : 'h',
            'c' : 'e',
            'd' : 's',
            'e' : 'o',
            'f' : 'c',
            'g' : 'v',
            'h' : 'x',
            'i' : 'd',
            'j' : 'u',
            'k' : 'i',
            'l' : 'g',
            'm' : 'l',
            'n' : 'b',
            'o' : 'k',
            'p' : 'r',
            'q' : 'z',
            'r' : 't',
            's' : 'n',
            't' : 'w',
            'u' : 'j',
            'v' : 'p',
            'w' : 'f',
            'x' : 'm',
            'y' : 'a',
            'z' : 'q',
            ' ' : ' '}

for case in range(num_cases):
  answer = ""
  
  input = in_file.readline().strip()
  
  for char in input:
    answer += MAPPINGS[char]
    
  out_file.write("Case #%s: %s\n" % (case + 1, answer))
    
in_file.close()
out_file.close()

print "Done!"