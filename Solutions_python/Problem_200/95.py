def phase():
    return input()

def largest_tidy(int_str):
    number_recoder = "0"
    out_put = "0"
    is_increasing = True
    for s in int_str:
        if is_increasing:
            if number_recoder <= s:
                number_recoder = s
                out_put += s
            else:
                out_put += "9"
                for i in range(1, len(out_put) - 1):
                    if out_put[-(i+2)] == number_recoder:
                        out_put = out_put[:-(i+1)] + "9" + out_put[-i:]
                    else:
                        out_put = str(int(out_put) - 10**int(i))
                        break
                is_increasing = False
        else:
            out_put += "9"

    return int(out_put)

def main():
    test_times = int(input())
    for t in range(1, test_times + 1):
        input_number_str = phase()
        print ("Case #%d: %d" %(t, largest_tidy(input_number_str)))
        

if __name__ == '__main__':
    main()