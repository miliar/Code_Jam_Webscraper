class SearchEngPop:
    def __init__(self,se_names):
        self.names = se_names
        
        self.nat_val = {}
        idx = 0
        for name in self.names:
            self.nat_val[name] = idx
            idx += 1

    def name_idx(self,name):
        return self.nat_val[name]

    def __getitem__(self,i):
        return self.names[i]

    def __len__(self):
        return len(self.names)

class QueryList:
    def __init__(self,se_pop,queries):
        self.sep = se_pop
        self.q_names = queries

        self.q_nats = [self.sep.name_idx(name) for name in self.q_names]
        
    def __len__(self):
        return len(self.q_names)

    def __getitem__(self,i):
        return self.q_names(i)

    def max_elt(lst):
        mx = lst[0]
        mx_idx = 0
        for i in range(1,len(lst)):
            if lst[i] > mx:
                mx,mxidx = lst[i],i
        return (mx,mx_idx)
    max_elt = staticmethod(max_elt)

    def swaps(self):
        subseq_mat = []
        for i in range(len(self)):
            subseq_mat.append([])
            for j in range(len(self.sep)):
                if self.sep[j] == self.q_names[i]:
                    subseq_mat[i].append(0)
                if self.sep[j] != self.q_names[i]:
                    if i == 0:
                        subseq_mat[i].append(1)
                    else:
                        subseq_mat[i].append(subseq_mat[i-1][j]+1)
    
        swap_count = -1
        cur_row = len(self)-1
        while cur_row >= 0:
            max_val,max_idx = QueryList.max_elt(subseq_mat[cur_row])
            swap_count += 1
            cur_row = cur_row - max_val

        return swap_count

class FileParser:
    def __init__(self):
        in_file = open(raw_input('Enter the input file name: '),'r')
        out_file = open(raw_input('Enter the output file name: '),'w')
        
        num_cases = int(in_file.readline())
        for c in range(num_cases):
            num_se = int(in_file.readline())
            se_names = []
            for x in range(num_se):
                se_names.append(in_file.readline())
            sep = SearchEngPop(se_names)
            
            num_q = int(in_file.readline())
            q_names = []
            for x in range(num_q):
                q_names.append(in_file.readline())
            q_lst = QueryList(sep,q_names)

            swap_val = q_lst.swaps()
            if num_q == 0:
                swap_val = 0
            out_file.write('Case #'+str(c+1)+': '+str(swap_val)+'\n')
        in_file.close()
        out_file.close()

fp = FileParser()
