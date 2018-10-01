#-*- coding: utf-8 -*-

def solve(N):

    if N < 10:
        return N

    # verifica se é tudo igual ou na ordem
    S = [int(x) for x in str(N)]
    previous = S[0]

    index = 0
    count = len(S)
    remainder = count

    for current in S[1:]:
        
        index = index + 1
        remainder = remainder - 1

        if current >= previous:
            previous = current
        else:

            if previous == 1:
                return "9" * (count - 1)

            else:
                
                _S = S[index-1::-1]
                

                if len(_S) == 1:
                    return str(_S[0]-1) + "9" * (count-1)

                elif len(_S) == 2 and _S[0] == _S[1]:
                    return str(_S[1]-1) + "9" * (count-1)
                else:
                    #print index, _S

                    _index = 0    
                    _current = _S[0]

                    for _next in _S[1:]:

                        _current = _current - 1
                        _index = _index + 1
                        
                        #print _current < _next

                        if _current < _next:
                            _current = _next
                        else:
                            l = _S[:_index-1:-1]
                            #print l
                            return "".join(map(str, l)) + str(_current) + "9" * (count - len(l) -1)

                    # satanas :D
                    print _S, _index, _current, _next
                    break




    return N
            


T = int(raw_input())

case = 1

while case <= T:
    line = raw_input()
    N = int(line)
    print "Case #%d: %s" % (case, str(solve(N)))
    case = case + 1