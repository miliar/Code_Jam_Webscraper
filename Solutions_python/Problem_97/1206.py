def read_int(file_handle, eol="\n"):
    return int(file_handle.readline().rstrip(eol))

def read_str(file_handle, eol="\n"):
    return file_handle.readline().rstrip(eol)
    
def read_int_list(file_handle, eol="\n", delimiter=" "):
    return [int(i) for i in file_handle.readline().rstrip(eol).split(delimiter)]

def read_str_list(file_handle, eol="\n", delimiter=" "):
    return [s for s in file_handle.readline().rstrip(eol).split(delimiter)]
    
def read_int_dict(file_handle, eol="\n", delimiter=" "):
    pos = 0
    d = {}
    for i in file_handle.readline().rstrip(eol).split(delimiter):
        d[int(i)] = pos
        pos += 1
    return d
    
size = 0;
name = "numbers"
size_text = ['small', 'large', 'example']
f = open('%s_%s.in' % (name, size_text[size]), 'rb')
fo = open('%s_%s.out' % (name, size_text[size]), 'wb')

T = read_int(f)
for i in xrange(1, T+1):
    A,B = read_int_list(f)
    count = 0
    for m in xrange(max(A, 10), B+1):
        m_str = str(m)

        used = {}
        for j in xrange(0, len(m_str) - 1):
            # Cycle through possibles
            m_str = "%s%s" % (m_str[1:], m_str[0])
            
            # Avoid duplicates
            if (used.has_key(m_str)):
                continue
            else:
                used[m_str] = 0
            
            # Avoid leading zeros
            if (m_str[0] == "0"):
                continue
            
            # Count recycled numbers
            n = int(m_str)
            if ((m > n) and (A <= n)):
                count += 1

    output = "Case #%d: %d\n" % (i, count)
    print output
    fo.write(output)

f.close()
fo.close()