def main(filename):
    
    f = open(filename)
    out = open('snapper_large.out', 'w')
    counter = 1
    case_number = 0
    for line in f:
        if counter == 1:
            T = int(line.strip())
        else:
            case_number += 1
            N = int(line.split()[0])
            K = int(line.split()[1])
            output = snapper(N, K)
            if not output:
                output_line = "Case #%d: ON\n" % case_number
            else:
                output_line = "Case #%d: OFF\n" % case_number
                
            out.write(output_line)
        counter += 1

def snapper(N, K):
    
    return (K + 1) % (2 ** N)
    
if __name__ == "__main__":
    
    main('A-large.in')