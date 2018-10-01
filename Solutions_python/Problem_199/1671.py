f = open ('A-large.in', 'r');

cases = int(f.readline());
case = 0;
output = "";
while case < cases:
    case += 1;

    data, k = f.readline().split();
    k = int(k);

    sol = list(data.replace("-", "+"));
    data = list(data);

    result = 0;

    while data != sol:
        pos = data.index("-");
        if pos > len(data) - k:
            result = "IMPOSSIBLE";
            break;
        result += 1;
        for i in range(pos, pos+k):
            if data[i] == "-":
                data[i] = "+";
            else:
                data[i] = "-";
    
    output += "Case #" + str(case) + ": " + str(result) + "\n"

with open('A-large.out', 'w') as o:
    o.write(output)
