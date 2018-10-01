import math

def is_palindrome(number):
        lst = list(str(number))
        length = len(lst)
        if length == 1:
                return True
        else:
                for i in range(0, length/2):
                        j = length - i - 1
                        if lst[i] != lst[j]:
                                return False
        return True

def is_square(number):
        sqrt = math.sqrt(number)
        return math.ceil(sqrt) == math.floor(sqrt)

def gen_palindromes(size):
        if size == 1:
                return range(0, 10)
        elif size == 2:
                return [11,22,33,44,55,66,77,88,99]
        elif size % 2 == 0:
                lst = []
                for i in range(10**((size/2)-1), 10**((size/2))):
                        l = list(str(i))
                        m = l[:]
                        m.reverse()
                        lst.append(int("".join(l + m)))
                return lst
        else:
                lst = []
                lower = gen_palindromes(size-2)
                for l in lower:
                        for num in range(1, 10):
                                tmp = []
                                tmp.append(str(num))
                                tmp.append(str(l))
                                tmp.append(str(num))
                                lst.append(int("".join(tmp)))
                return lst

def get_palindromes_in_range(min, max):
        lst = []
        for i in range(len(str(min)), len(str(max))+1):
                lst = lst + gen_palindromes(i)
        ret = [x for x in lst if x >= min and x <= max]
        ret.sort()
        return ret
