def dic_reset(list):
    dic = {}
    for e in list:
        dic.setdefault(e)
    return dic
def switch(r1):
    engine_dic  = {}
    engine_list = []
    num_of_engine = int(r1.readline())
    for x in xrange(num_of_engine):
        line = r1.readline().strip()
        engine_list.append(line)
        #engine_dic.setdefault(line)
    engine_dic = dic_reset(engine_list)
    num_of_query = int(r1.readline())
    
    count = 0
    for x in xrange(num_of_query):
        line = r1.readline().strip()
        if engine_dic.has_key(line):
            del engine_dic[line]
            if len(engine_dic)== 0:
                count += 1
                engine_dic = dic_reset(engine_list)
                del engine_dic[line]
    return count
def main():
    #r1 = open("A-small-attempt0.in")
    r1 = open("A-large.in")
    case_str = r1.readline()
    case_num = int(case_str)
    for x in xrange(case_num):
        count = switch(r1)
        print "Case #%d: %d"%(x+1, count)
        
main()
