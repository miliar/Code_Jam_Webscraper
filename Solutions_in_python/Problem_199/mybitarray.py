import bitarray

class bitarray(bitarray.bitarray):
    def __hash__(self):
        return hash(self.tobytes())
