if __name__ == "__main__":
    in_f = open("B-large.in", "r")
    out_f = open("B.output", "w")
    for lineno, line in enumerate(in_f):
        if lineno == 0:
            continue
        
        line = line.strip()
        parts = [int(x) for x in line.split()]
        n, s, p = parts[:3]
        numbers = parts[3:]
        count = 0
        if p < 2:
            for number in numbers:
                if number >= p:
                    count += 1
        else:
            min_score = p * 3 - 4
            max_score = p * 3 - 2
            for number in numbers:
                if number >= max_score:
                    count += 1
                elif number >= min_score and s > 0:
                    s -= 1
                    count += 1
            
        outline = "Case #%s: %s\n" % (lineno, count)
        out_f.write(outline)
    
    in_f.close()
    out_f.close()
                