import sys



def get_case_input(inf):
    rows = []
    for j in range(2):
        r_no = int(inf.readline())
        for i in range(4):
            row = inf.readline()
            if i+1 == r_no:
                r = row.strip().split(' ')
                rows.append(r)

    return rows 




def main():
    infile = sys.argv[1]
    inf = open(infile, 'r')
    n_cases =  int(inf.readline())


    outfile = "magic_out.txt"
    outf = open(outfile, 'w')


    for each in range(n_cases):
        in_params = get_case_input(inf)
        intersect = list(set(in_params[0]) & set(in_params[1]))
        if len(intersect) == 0:
            ans = 'Volunteer cheated!'
        elif len(intersect) > 1:
            ans = 'Bad magician!'
        else:
            ans = intersect[0]

        outline = 'Case #%s: %s'%(each+1, ans)
        print outline
        outf.write(outline+'\n')

    outf.close()
    inf.close()


if __name__ == "__main__":
    main()
