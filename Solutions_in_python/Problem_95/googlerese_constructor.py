mappings = {}

def print_mappings():
    for i in xrange(26):
        if mappings.has_key(chr(ord('a') + i)):
            print mappings[chr(ord('a') + i)],
        else:
            print '_',
    print ''

while True:
    encrypted = raw_input("Gimmeh encrypted: ")
    decrypted = raw_input("Gimmeh decrypted: ")
    for i in xrange(len(encrypted)):
        if encrypted[i] != ' ':
            mappings[encrypted[i]] = decrypted[i]
    print_mappings()
    
