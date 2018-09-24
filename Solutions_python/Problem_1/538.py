def solve(engine,search):
    max_ind = 0
    no_of_switch = 0
    while True:
        for elem in engine:
            try:
                if search.index(elem)>max_ind:
                    max_ind=search.index(elem)
            except ValueError:
                return no_of_switch
        search = search[max_ind:len(search)]
        no_of_switch = no_of_switch +1
        max_ind = 0

def universe():
    f = open("A-large.in")
    fout = open("A-large.out","w")
    engine = []
    engine_index = 1
    search_index = 0
    no_of_engines = 0
    no_of_search = 0
    search = []
    try:
        i = 0
        knauter = 1
        for line in f:
            if i==0:
                #omit last \n
                no_cases = int(line[0:len(line)-1])
            elif i==engine_index:
                if i!=1:
                    fout.write("Case #"+str(knauter)+": "+str(solve(engine,search))+"\n")
                    knauter = knauter +1
                engine =[]
                search = []
                no_of_engines = int(line[0:len(line)-1])
                search_index = no_of_engines+1+i
            elif i==search_index:
                no_of_search = int(line[0:len(line)-1])
                engine_index = no_of_search+1+i
            elif (i > search_index) and (i < engine_index):
                search.append(line[0:len(line)-1])
            elif (i > engine_index) and (i < search_index):
                engine.append(line[0:len(line)-1])
            i=i+1
        fout.write("Case #"+str(knauter)+": "+str(solve(engine,search))+"\n")
    finally:
        f.close()
        fout.flush()
        fout.close()
if __name__ == "__main__":
    universe()

