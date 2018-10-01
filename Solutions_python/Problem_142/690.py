
def get_m(s):
    new_str = []
    m_str = ""
    c_list = []
    ch = s[0]
    count = 0
    for c in s:
        if c == ch:
            count += 1
        else:
            out = (ch, count)
            m_str += ch
            c_list.append(count)
            new_str.append(out)
            ch = c
            count = 1
    out = (ch, count)
    m_str += ch
    c_list.append(count)
    new_str.append(out)

    assert len(c_list) == len(m_str)

    # print s, "--->", m_str, c_list
    return m_str, c_list

def get_output(strs, N):
    m_strs = []
    c_lists = []
    for i in range(N):
        m_str, c_list = get_m(strs[i])
        m_strs.append(m_str)
        c_lists.append(c_list)

    first_m = m_strs[0]
    n = len(first_m)
    for i in range(N):
        if m_strs[i] != first_m:
            return "Fegla Won"

    # calculate min changes
    changes = 0
    for i in range(n):
        ns = [c_list[i] for c_list in c_lists]
        avg = sum(ns) / len(ns)
        cg = [abs(avg - n) for n in ns]
        changes += sum(cg)
    return changes
# main begins
T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    strs = []
    for _ in range(N):
        s = raw_input().strip()
        strs.append(s)

    output = get_output(strs, N)
    print "Case #%s: %s" % ((i + 1), output)