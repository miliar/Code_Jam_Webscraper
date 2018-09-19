def calculate(int a, int b, probs):
    result = []
    for bs in range(0, a):
        rem = a-bs
        p_correct = 1.0
        for y in range(rem):
            p_correct *= probs[y]
        correct_kp = (b-a+2*bs+1)
        incorrect_kp= correct_kp + (b+1)
        result.append(p_correct*correct_kp+(1.0-p_correct)*incorrect_kp)
    return result

